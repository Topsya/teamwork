from setuptools import setup, find_namespace_packages
setup(
    name="personal assistant Tech_Titans",
    version= "0.1",
    description= " Proekt rabotae s phon book , notebook, clean papki po formats ",
    url='https://github.com/Topsya/teamwork-Tech_Titans',
    author= "Anton Mescheryakov, Denis Mashtak, Elizaveta Kolesnyk, Oleg Dovhyi",
    author_email= "topsya1986@gmail.com,  ned.warov@gmail.com,  kolesnyk.elyzaveta24.1201@gmail.com,  oleg.dovgyy@gmail.com",
    packages= find_namespace_packages(),
    include_package_data=True,
    entry_points={
          "console_scripts": ["clean-folder=Clean_folders.start:clean_folder"]
          }
)