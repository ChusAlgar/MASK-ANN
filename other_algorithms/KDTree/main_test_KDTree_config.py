from experiments.load_train_test_set import *
from experiments.neighbors_utils import *
from other_algorithms.KDTree.KDTree_npdist import KDTree_nn_index, KDTree_nn_search
import logging
from timeit import default_timer as timer


def KDTree(config):

    # Read test parameters
    dataset = config.get('test', 'dataset')
    k = config.getint('test', 'k')
    distance = config.get('test', 'distance')  # Possible values:
                                 # From scikit-learn: ['cityblock', 'cosine', 'euclidean', 'l1', 'l2', 'manhattan']. These metrics support sparse matrix inputs. ['nan_euclidean'] but it does not yet support sparse matrices
                                 # From scipy.spatial.distance: ['braycurtis', 'canberra', 'chebyshev', 'correlation', 'dice', 'hamming', 'jaccard', 'kulsinski', 'mahalanobis', 'minkowski', 'rogerstanimoto', 'russellrao', 'seuclidean', 'sokalmichener', 'sokalsneath', 'sqeuclidean', 'yule']bThese metrics do not support sparse matrix inputs.
    method = config.get('test', 'method')



    # Set log configuration
    logging.basicConfig(filename="./experiments/logs/" + dataset + "/test_knn_" + dataset + "_" + str(k) + "_" + distance + "_" + method + ".log", filemode='w', format='%(asctime)s - %(name)s - %(message)s', level=logging.INFO)
    logging.info('------------------------------------------------------------------------')
    logging.info('                          KNN Searching')
    logging.info('------------------------------------------------------------------------\n')
    logging.info("")
    logging.info("---- Searching the " + str(k) + " nearest neighbors within " + method + " over " + str(
        dataset) + " dataset using " + str(distance) + " distance. ----")


    # Regarding the dataset name, set the file name to load the train and test set
    file_name = "./data/" + str(dataset) + "_train_test_set.hdf5"

    # Load the train and test sets to carry on the experiments
    # train_set, test_set = load_train_test(str(dataset))
    train_set, test_set = load_train_test_h5py(file_name)

    # GENERATE INDEX AND CENTROIDS
    # AND FIND THE KNN FROM THE train_set OF THE ELEMENTS CONTAINED IN THE test_set, USING DISTANCE CHOOSEN

    # Using KDTree Algorithm, build the index of nearest neighbors
    start_time_i = timer()
    knn_index = KDTree_nn_index(train_set, distance)
    end_time_i = timer()
    logging.info('Index time= %s seconds', end_time_i - start_time_i)

    # Store index on disk to obtain its size
    # with open("./other_algorithms/KDTree/" + dataset + str(k) +".pickle", 'wb') as handle:
    #    dump(knn_index, handle)

    # Using KDTree Algorithm and the index built, find the k nearest neighbors
    start_time_s = timer()
    indices, coords, dists = KDTree_nn_search(train_set, test_set, k, knn_index)
    end_time_s = timer()
    logging.info('Search time = %s seconds\n', end_time_s - start_time_s)
    logging.info('Average time spended in searching a single point = %s',
                 (end_time_s - start_time_s) / test_set.shape[0])
    logging.info('Speed (points/s) = %s\n', test_set.shape[0] / (end_time_s - start_time_s))

    # Regarding the knn, method, dataset_name and distance choosen, set the file name to store the neighbors
    file_name = "./experiments/NearestNeighbors/" + dataset + "/knn_" + dataset + "_" + str(k) + "_" + distance + "_" + method + ".hdf5"

    # Store indices, coords and dist into a hdf5 file
    save_neighbors(indices, coords, dists, file_name)

    # Print
    # print_knn(train_set, test_set, coords, dataset_name, d, "KDTree", k)

    logging.info('------------------------------------------------------------------------\n')
