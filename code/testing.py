from PrincipleComponentAnalysis import PrincipleComponentAnalysis
from ColorMoments import CM
from SIFT import SIFT
from SingularValueDecomposition import SVD
from LatentDirichletAllocation import LDA
from NonNegativeMatrix import NM_F
from SimilarSubject import Subjects

#md = SIFT("../Hands/Hand_0000002.jpg")

#md.createKMeans("../output/SIFT",30)

pca1 = PrincipleComponentAnalysis()
lda1 = LDA()
svd1 = SVD()
nmf1 = NM_F()

#task1
        # pca1.createPCA_KLatentSemantics("LBP", 20)
        # pca1.createPCA_KLatentSemantics("LBP", 10)

# query 1
svd1.createKLatentSymantics("SIFT", 20)
# query 2
svd1.createKLatentSymantics("SIFT", 40)
# query 3
lda1.createKLatentSymantics("CM", 20)
# query 4
lda1.createKLatentSymantics("CM", 40)

pca1.createPCA_KLatentSemantics("HOG", 10)
pca1.createPCA_KLatentSemantics("HOG", 20)
pca1.createPCA_KLatentSemantics("HOG", 30)
pca1.createPCA_KLatentSemantics("HOG", 40)
        # lda1.createKLatentSymantics("LBP", 20)
        # lda1.createKLatentSymantics("LBP", 10)


lda1.createKLatentSymantics("CM", 30)

        # svd1.createKLatentSymantics("LBP", 20)
        # svd1.createKLatentSymantics("LBP", 10)

svd1.createKLatentSymantics("SIFT", 10)

svd1.createKLatentSymantics("SIFT", 30)

        # nmf1.createKLatentSymantics("LBP", 20)

nmf1.createKLatentSymantics("LBP", 10)
nmf1.createKLatentSymantics("LBP", 30)

#task2
        # pca1.mSimilarImage("./phase2_Images/Hand_0000200.jpg", "LBP", 20, 10)
        # pca1.mSimilarImage("./phase2_Images/Hand_0000200.jpg", "LBP", 10, 10)
        # pca1.mSimilarImage("./phase2_Images/Hand_0000200.jpg", "HOG", 10, 10)

# query 1
pca1.mSimilarImage("./phase2_Images/Hand_0000111.jpg", "HOG", 10, 10)
# query 2
pca1.mSimilarImage("./phase2_Images/Hand_0000111.jpg", "HOG", 40, 10)
        # lda1.mSimilarImage("./phase2_Images/Hand_0000200.jpg", "LBP", 20, 10)
        # lda1.mSimilarImage("./phase2_Images/Hand_0000200.jpg", "LBP", 10, 10)
        # svd1.mSimilarImage("./phase2_Images/Hand_0000200.jpg", "LBP", 20, 10)
        # svd1.mSimilarImage("./phase2_Images/Hand_0000200.jpg", "LBP", 10, 10)
        # nmf1.mSimilarImage("./phase2_Images/Hand_0000200.jpg", "LBP", 20, 10)

# query 3
nmf1.mSimilarImage("./phase2_Images/Hand_0000200.jpg", "LBP", 10, 10)
# query 4
nmf1.mSimilarImage("./phase2_Images/Hand_0000200.jpg", "LBP", 40, 10)

#task3

# query 1
pca1.LabelLatentSemantic("dorsal", "HOG", 20)
# query 2
pca1.LabelLatentSemantic("dorsal", "HOG", 30)
        # pca1.LabelLatentSemantic("left", "CM", 20)
        # lda1.LabelLatentSemantic("dorsal", "HOG", 20)

# query 3
lda1.LabelLatentSemantic("left", "CM", 20)
# query 4
lda1.LabelLatentSemantic("left", "CM", 30)
        # svd1.LabelLatentSemantic("dorsal", "HOG", 20)
        # svd1.LabelLatentSemantic("left", "CM", 20)
        # nmf1.LabelLatentSemantic("dorsal", "HOG", 20)
        # nmf1.LabelLatentSemantic("left", "CM", 20)

#task4
        # pca1.mSimilarImage_Label("./phase2_Images/Hand_0000200.jpg", "palmar", "LBP", 10, 20)
        # pca1.mSimilarImage_Label("./phase2_Images/Hand_0011160.jpg", "Access", "SIFT", 10, 10)
        # lda1.mSimilarImage_Label("./phase2_Images/Hand_0000200.jpg", "palmar", "LBP", 10, 10)
        # lda1.mSimilarImage_Label("./phase2_Images/Hand_0011160.jpg", "Access", "SIFT", 10, 10)
        # svd1.mSimilarImage_Label("./phase2_Images/Hand_0000200.jpg", "palmar", "LBP", 10, 10)

# query 1
nmf1.mSimilarImage_Label("./phase2_Images/Hand_0000200.jpg", "palmar", "LBP", 10, 10)
# query 2
nmf1.mSimilarImage_Label("./phase2_Images/Hand_0000200.jpg", "palmar", "LBP", 30, 10)
# query 3
svd1.mSimilarImage_Label("./phase2_Images/Hand_0011160.jpg", "Access", "SIFT", 10, 10)
# query 4
svd1.mSimilarImage_Label("./phase2_Images/Hand_0011160.jpg", "Access", "SIFT", 10, 10)

        # nmf1.mSimilarImage_Label("./phase2_Images/Hand_0011160.jpg", "Access", "SIFT", 10, 10)


#task5
        # pca1.ImageClassfication("./phase2_Images/Hand_0000111.jpg", "LBP", 20)

# query1
nmf1.ImageClassfication("./phase2_Images/Hand_0000111.jpg", "LBP", 10)
# query2
nmf1.ImageClassfication("./phase2_Images/Hand_0000111.jpg", "LBP", 30)
# query 3
svd1.ImageClassfication("./phase2_Images/Hand_0001395.jpg", "SIFT", 10)
# query 4
svd1.ImageClassfication("./phase2_Images/Hand_0001395.jpg", "SIFT", 30)

pca1.ImageClassfication("./phase2_Images/Hand_0001395.jpg", "SIFT", 20)
lda1.ImageClassfication("./phase2_Images/Hand_0000111.jpg", "LBP", 20)
        # lda1.ImageClassfication("./phase2_Images/Hand_0001395.jpg", "SIFT", 20)
        # svd1.ImageClassfication("./phase2_Images/Hand_0000111.jpg", "LBP", 20)

        # nmf1.ImageClassfication("./phase2_Images/Hand_0001395.jpg", "SIFT", 20)

# task6
# Query 1 Subject 27 and Query 2 Subject 55
s1 = Subjects()
s1.similar3Subjects('CM', 20, '27')
s1.similar3Subjects('LBP', 20, '27')
# s1.similar3Subjects('LBP', 20, '1000000')
# s1.similar3Subjects('LBP', 20, '1011')
# s1.similar3Subjects('LBP', 20, '1081')
s1.similar3Subjects('HOG', 20, '27')
s1.similar3Subjects('SIFT', 20, '27')
s1.similar3Subjects('CM', 20, '55')
s1.similar3Subjects('LBP', 20, '55')
s1.similar3Subjects('HOG', 20, '55')
s1.similar3Subjects('SIFT', 20, '55')

# task7
# Subject to Subject similarity
# Query 1 K value of 10 and Query 2 K value of 20
s1.createSSMatrix(10)
s1.createSSMatrix(20)

# task8
# Create binary image-metadata matrix
# Query 1 K value of 4 and Query 2 K value of 6
