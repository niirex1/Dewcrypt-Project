# feature_selection.py
# Feature selection algorithms for the DewCrypt model.

from sklearn.feature_selection import RFE
from sklearn.decomposition import PCA
from sklearn.svm import SVC

def recursive_feature_elimination(input_features, labels):
    """
    Recursive Feature Elimination algorithm as described in the paper.
    """
    estimator = SVC(kernel="linear")
    selector = RFE(estimator, n_features_to_select=3)
    selector = selector.fit(input_features, labels)
    return selector.support_

def principal_component_analysis(input_features):
    """
    Principal Component Analysis algorithm as described in the paper.
    """
    pca = PCA(n_components=2)
    pca.fit(input_features)
    return pca.transform(input_features)

if __name__ == "__main__":
    # Test the feature selection functions
    sample_features = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    sample_labels = np.array([0, 1, 0])
    print("Selected Features:", recursive_feature_elimination(sample_features, sample_labels))
    print("PCA Transformed Features:", principal_component_analysis(sample_features))
