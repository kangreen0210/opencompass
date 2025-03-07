import csv
import json
import os.path as osp
from os import environ
from datasets import load_dataset
import os
from datasets import Dataset, DatasetDict
from opencompass.datasets.supergpqa.supergpqa_utils import (
    evaluate_responses, find_file, load_json_or_jsonl,
    load_json_or_jsonl_with_idx, load_yaml)
from opencompass.openicl.icl_evaluator import BaseEvaluator
from opencompass.registry import ICL_EVALUATORS,LOAD_DATASET
import unittest
from opencompass.utils import get_data_path
from opencompass.datasets.supergpqa.supergpqa_eval import (extract_option_labels,extract_option_content)
from ..base import BaseDataset


def _parse(item, template, prompt_mode):
    prompt_format = [item['question']+'\n'+'\n'.join([f'{chr(65+i)}) {option}' for i, option in enumerate(item['options'])])]
    item['infer_prompt'] = template['prompt_format'][0].format(*prompt_format)
    item['prompt_mode'] = prompt_mode
    return item


@LOAD_DATASET.register_module()
class SuperGPQADataset(BaseDataset):
    @staticmethod
    def load(path: str, prompt_mode: str,category:str, **kwargs):
        path = get_data_path(path)
        dataset = load_dataset(path, split='train')
        dataset = dataset.filter(lambda x: x['subfield'] == category)

        #get prompt template
        template_path = None
        if prompt_mode == 'zero-shot':
            template_path = os.path.join(
                os.path.dirname(__file__),
                'supergpqa_dataset_config/prompt/zero-shot.yaml')
        elif prompt_mode == 'five-shot':
            template_path = os.path.join(
                os.path.dirname(__file__),
                'supergpqa_dataset_config/prompt/five-shot.yaml')
        try:
            template = load_yaml(template_path)
        except FileNotFoundError:
            print(f'[ERROR] Missing prompt template: {template_path}')
            return Dataset.from_list([])
        
        dataset =dataset.map(lambda item: _parse(item, template, prompt_mode))
        return dataset

@ICL_EVALUATORS.register_module()
class SuperGPQAEvaluator(BaseEvaluator):

    def __init__(self):
        super().__init__()

    def score(self,predictions, references,test_set):
        mode= test_set[0]['prompt_mode'] 
        acc = 0
        count = 0
        err = 0
        miss = 0
        acc_difficulty = {"hard": 0, "middle": 0, "easy": 0}
        count_difficulty = {"hard": 0, "middle": 0, "easy": 0}
        stats = {
            'discipline': {},
            'field': {},
            'subfield': {}
        }
        
        for i,sample in enumerate(test_set):
            prediction=predictions[i]
            gold=references[i]
            if mode == 'zero-shot':
                predict = extract_option_labels(prediction, 'ABCDEFGHIJ')
                if predict == None:
                    predict = extract_option_content(prediction, sample["options"])
                    predict = chr(sample["options"].index(predict) + 65) if predict else None
                sample["extracted_answer"] = predict
            elif mode == 'five-shot':
                response = prediction.split('Question:')[0]
                predict = extract_option_labels(response, 'ABCDEFGHIJ')
                if predict == None:
                    predict = extract_option_content(response, sample["options"])
                    predict = chr(sample["options"].index(predict) + 65) if predict else None
                if predict == None:
                    predict = extract_option_labels(prediction, 'ABCDEFGHIJ')
                    if predict == None:
                        predict = extract_option_content(prediction, sample["options"])
                        predict = chr(sample["options"].index(predict) + 65) if predict else None
                sample["extracted_answer"] = predict
            
            discipline = sample.get("discipline", "unknown")
            field = sample.get("field", "unknown")
            subfield = sample.get("subfield", "unknown")
            difficulty = sample.get("difficulty", "unknown")
            
            for level, key in [
                ('discipline', discipline),
                ('field', f"{discipline}/{field}"),
                ('subfield', f"{discipline}/{field}/{subfield}")
            ]:
                if key not in stats[level]:
                    stats[level][key] = {
                        "correct": 0, 
                        "total": 0, 
                        "miss": 0, 
                        "error": 0,
                        "discipline": discipline,
                        "field": field,
                        "subfield": subfield,
                        "difficulty": {
                            "easy": {"correct": 0, "total": 0},
                            "middle": {"correct": 0, "total": 0},
                            "hard": {"correct": 0, "total": 0}
                        }
                    }
                
                stats[level][key]["total"] += 1
                stats[level][key]["difficulty"][difficulty]["total"] += 1
                
                answer_letter = sample["answer_letter"]
                assert answer_letter==gold
                if predict and answer_letter == predict:
                    acc += 1
                    acc_difficulty[difficulty] += 1
                    sample["status"] = "correct"
                    stats[level][key]["correct"] += 1
                    stats[level][key]["difficulty"][difficulty]["correct"] += 1
                elif predict == None or predict == "":
                    miss += 1
                    sample["status"] = "miss"
                    stats[level][key]["miss"] += 1
                elif predict == 'error':
                    err += 1
                    sample["status"] = "error"
                    stats[level][key]["error"] += 1
                else:
                    sample["status"] = "incorrect"
                count += 1
                count_difficulty[difficulty] += 1
        
        return {
        'accuracy': acc / count if count > 0 else 0,
        # 'error_rate': err / count if count > 0 else 0,
        # 'miss_rate': miss / count if count > 0 else 0,
        # 'hard_accuracy': acc_difficulty["hard"] / count_difficulty["hard"] if count_difficulty["hard"] > 0 else 0,
        # 'middle_accuracy': acc_difficulty["middle"] / count_difficulty["middle"] if count_difficulty["middle"] > 0 else 0,
        # 'easy_accuracy': acc_difficulty["easy"] / count_difficulty["easy"] if count_difficulty["easy"] > 0 else 0
        }