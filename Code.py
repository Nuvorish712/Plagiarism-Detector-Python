import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# student_files = [doc for doc in os.listdir() if doc.endswith('.txt')]
# student_notes =[open(File).read() for File in  student_files]

def cmp(file1, file2):
    student_files = [file1, file2]
    student_notes =[open(File).read() for File in  student_files]

    vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
    similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])

    vectors = vectorize(student_notes)
    global s_vectors 
    s_vectors = list(zip(student_files, vectors))
    plagiarism_results = set()

    def check_plagiarism():
        global s_vectors
        for student_a, text_vector_a in s_vectors:
            new_vectors =s_vectors.copy()
            current_index = new_vectors.index((student_a, text_vector_a))
            del new_vectors[current_index]
            for student_b , text_vector_b in new_vectors:
                sim_score = similarity(text_vector_a, text_vector_b)[0][1]
                sim = str(round(sim_score*100, 3))
                student_pair = sorted((student_a, student_b))
                s1 = os.path.basename(student_pair[0])
                s2 = os.path.basename(student_pair[1])
                f1 = "File 1: "+s1
                f2 = "File 2: "+s2
                # sim1 = "\nSimilarities: "+sim
                sim = "Similarities: "+sim+"%"
                score = (f1+"\n"+f2+"\n"+sim)
                plagiarism_results.add(score)
        return plagiarism_results

    for data in check_plagiarism():
        print(data)