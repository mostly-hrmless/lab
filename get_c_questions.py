#!/usr/bin/python3

import os, sys, subprocess, random

avoid_these = ['.DS_Store', 'VS_SLN_Template']

googletest_url = 'https://github.com/google/googletest.git'
basic_dev_url = 'https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file'
proj_path = os.path.abspath('./')
C_path = '.testbank/performance/C_Programming'

def cleanTest():
    if os.path.exists('C_Programming'):
        subprocess.call('rm -rf C_Programming'.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.call('mkdir C_Programming'.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def getQuestions():
    questions = ['c_linked_list', 'string_copying']
    return questions

    
def copyQuestionToTest(questions):
    for question in questions:
        subprocess.call(['cp', '-r', os.path.join(proj_path, C_path, question), 'C_Programming/'])
        if not os.path.exists(f'C_Programming/{question}/googletest'):
            subprocess.call(['cp', '-r', f'{proj_path}/googletest', f'C_Programming/{question}/'])

def main():
    cleanTest()
    
    if not os.path.exists('googletest'):
        subprocess.call(['git', 'clone', googletest_url])

    if not os.path.exists(".testbank"):
        subprocess.call(['git', 'clone', basic_dev_url, '.testbank'])
    
    copyQuestionToTest(getQuestions())

    return 0

if __name__ == "__main__":
    main()
