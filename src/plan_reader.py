import json
import os


current_file_path = os.path.dirname(__file__)
ALL_PLAN_PATH = os.path.join(current_file_path, '../resources/all_plans.json')

with open(ALL_PLAN_PATH, "r") as f:
    all_plan_dict = json.load(f)

