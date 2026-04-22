#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
import pytest
import shutil  # 新增，用来删除文件夹

if __name__ == '__main__':
    # 切换到证据目录下
    dirname = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(dirname)
    os.chdir(root_dir)

    print(f"✅ 已自动切换到项目根目录: {root_dir}")

    # 证据目录下存在报告文件就递归删除，再创建一个
    reports = os.path.join(root_dir, "reports")
    if os.path.exists(reports):
        shutil.rmtree(reports)
        print("🗑️  已清空旧的 reports 文件夹")
    os.makedirs(reports, exist_ok=True)

    pytest.main([
        "-vs",

        "--alluredir=./reports"
    ])

    print("\n🎉 报告生成完成！输入命令打开：")
    print("allure serve ./reports")