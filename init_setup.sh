echo [$(date)]: "START"
echo [$(date)]: "creating environment"
conda create --prefix ./env python=3.7 -y
echo [$(date)]: "activate environment"
conda activate ./env
echo [$(date)]: "installing requirements"
pip install -r requirements.txt
echo [$(date)]: "export conda environment"
conda env export > conda.yaml
echo [$(date)]: "add env to gitignore"
echo "env/" > .gitignore
echo [$(date)]: "installing setup.py"
pip install -e .
echo [$(date)]: "Creating Office Commute application Django"
django-admin startproject office_commute_app
echo [$(date)]: "Creating user authentication app Django"
python manage.py startapp user_authentication
echo [$(date)]: "initiall setup is done!!"
