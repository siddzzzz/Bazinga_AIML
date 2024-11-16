import pickle
from PyPDF2 import PdfReader
import re

def Job(txt):
    clf = pickle.load(open('Models/clf.pkl', 'rb'))
    tfidf = pickle.load(open('Models/tfidf.pkl', 'rb'))
    def remove_stopwords(text):
        """
        Remove stopwords from a given text.
        Parameters:
            text (str): The input text from which to remove stopwords.
            language (str): The language of the stopwords. Default is 'english'.
        Returns:
            filtered_text (str): Text without stopwords.
        """
        
        stop_words = set([
        "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", 
        "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", 
        "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", 
        "theirs", "themselves", "what", "which", "who", "whom", "this", "that", 
        "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", 
        "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", 
        "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", 
        "at", "by", "for", "with", "about", "against", "between", "into", "through", 
        "during", "before", "after", "above", "below", "to", "from", "up", "down", 
        "in", "out", "on", "off", "over", "under", "again", "further", "then", 
        "once", "here", "there", "when", "where", "why", "how", "all", "any", 
        "both", "each", "few", "more", "most", "other", "some", "such", "no", 
        "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", 
        "t", "can", "will", "just", "don", "should", "now"
        ])
        words = text.split()  # Simple tokenization by spaces
        filtered_words = [word for word in words if word.lower() not in stop_words]
        filtered_text = ' '.join(filtered_words)
        return filtered_text
    def cleanResume(txt):
        """
        Clean the text in the resume i.e. remove unwanted chars in the text. For e.g. 
        1 URLs,
        2 Hashtags,
        3 Mentions,
        4 Special Chars,
        5 Punctuations
        Parameters:
            resume_text (str): The input resume text to be cleaned.
        Returns:
            clean_text (str): Clean Resume.
        """
        cleanText = re.sub('http\S+\s', ' ', txt)
        cleanText = re.sub('RT|cc', ' ', cleanText)
        cleanText = re.sub('#\S+\s', ' ', cleanText)
        cleanText = re.sub('@\S+', '  ', cleanText)  
        cleanText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
        cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText) 
        cleanText = re.sub('\s+', ' ', cleanText)
        cleanText  = remove_stopwords(cleanText)
        return cleanText
    

    resume = txt
    
    category_mapping = {
        15: "Java Developer",
        23: "Testing",
        8: "DevOps Engineer",
        20: "Python Developer",
        24: "Web Designing",
        12: "HR",
        13: "Hadoop",
        3: "Blockchain",
        10: "ETL Developer",
        18: "Operations Manager",
        6: "Data Science",
        22: "Sales",
        16: "Mechanical Engineer",
        1: "Arts",
        7: "Database",
        11: "Electrical Engineering",
        14: "Health and fitness",
        19: "PMO",
        4: "Business Analyst",
        9: "DotNet Developer",
        2: "Automation Testing",
        17: "Network Security Engineer",
        21: "SAP Developer",
        5: "Civil Engineer",
        0: "Advocate",
    }
    cleaned_resume = cleanResume(resume)

    input_features = tfidf.transform([cleaned_resume])

    prediction_id = clf.predict(input_features)[0]

    category_name = category_mapping.get(prediction_id, "Unknown")

    return category_name

