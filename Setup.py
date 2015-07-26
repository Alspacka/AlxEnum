'''
Created on Jun 18, 2015

@author: Alexander Van Daele
'''

import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

if __name__ == '__main__':
    setup(name='AlxEnum', version='0.1', description='Simple collection of enum scripts.', 
          author='Alexander Van Daele',author_email='xalspacka@gmail.com', url='https://github.com/Alspacka/AlxEnum', 
          scripts=['AlxEnum','LinuxPrivEsc','WindowsPrivEsc'],long_description=read('README.md'), 
          packages=['Common', 'PrivilegeEscLinux','PrivilegeEscWindows','ScanModules','Scanner'],
          data_files=[('/usr/share/AlxEnum', ['LICENSE','AlxEnumConfig.xml']), ('/usr/share/man/man1', ['Manual/AlxEnum.1.gz'])])