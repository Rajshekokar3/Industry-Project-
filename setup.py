from setuptools import find_packages,setup
from typing import List 

HYPERN_E_DOT='-e .'

def get_requirements(filepath:str)->List[str]:
        '''
        this functin will return the list of requirement
        '''

        requirements=[]
        with open(filepath)  as file_obj:  #this actually createthe/n at the end
            requirements=file_obj.readlines()
            #what we will do we will replace the /n to blank 
            requirements=[req.replace("\n","")for req in requirements]


            if HYPERN_E_DOT in requirements:
                  requirements.remove(HYPERN_E_DOT)

        return requirements


setup(
name="mlproject",
version='0.0.1',
author='Raj',
author_email="rajshekokar3@gmail.com",
packages=find_packages(),
#install_requires=['pandas','numpy','searborn']
install_requires=get_requirements("requirements.txt")

)
# it use whentyou ahve mutiple  of  library or we can say that good number of libraray to install
#install_requires=get_requiremnets("requirement.txt")