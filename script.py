import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("--------------Installation Start-----------------------\n")


# Install pandas
install('numpy')
install('pandas')
install('matplotlib')
install('seaborn')
install('nltk')
install('scikit-learn')
install('IPython')



# nltk extensions
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


print("--------------Installalation Done-----------------------")