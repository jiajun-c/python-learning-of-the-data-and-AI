from sklearn.datasets import make_regression
from sklearn.datasets import make_classification
from sklearn.datasets import make_hastie_10_2

features, target, coefficient = make_regression(n_samples=100,
                                                n_features=3,
                                                n_informative=3,
                                                n_targets=1,
                                                noise=0.0,
                                                coef=True,
                                                random_state=1)

print("Feature Matrix{}\n Target Vector{}\n".format(features[:3], target[:3]))

features, target = make_classification(n_samples=100,
                                       n_features=3,
                                       n_informative=3,
                                       n_redundant=0,
                                       n_classes=2,
                                       weights=[.25, .75],
                                       random_state=1)
print("Feature Matrix{}\n Target Vector{}\n".format(features[:3], target[:3]))
