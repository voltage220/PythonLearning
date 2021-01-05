import os
from shutil import copyfile

path = "2020摄影比赛"
targetDir = "所有照片"

def copy_to_new(source_name, target_name):
    print("Copy: ", source_name, " [To]:", target_name)
    copyfile(source_name, target_name)

def rename_with_account(old_name, account_name):
    print("Rename: ", old_name, " [To]:", account_name)
    os.rename(old_name, account_name)

def rename_with_accout_no():
    dir_list = os.listdir(path)
    for account in dir_list:
        for root, dirs, files in os.walk(os.path.join(path, account)):
            for file in files:
                pre = f"{account}"
                target_name = os.path.join(targetDir, f"{file}")
                account_name = os.path.join(root, f"{file}")
                if (file.find(pre) == -1):
                    target_name = os.path.join(targetDir, f"{pre}_{file}")
                    account_name = os.path.join(root, f"{pre}_{file}")
                copy_to_new(os.path.join(root, file), target_name)
                rename_with_account(os.path.join(root, file), account_name)

rename_with_accout_no()
