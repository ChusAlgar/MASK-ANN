import logging
import kmeans_tree_nparray_geodata as kt


logging.basicConfig(filename='result_kmtnp_testCapacity-100_geodata.log', filemode='w', format='%(asctime)s - %(name)s - %(message)s',
                    level=logging.INFO)

# Parámetros de entrada comunes a todas las simulaciones:

# SubText 1
logging.info('------------------------------------------------------------------------')
logging.info(' ')
tam_grupo = 100   #16
n_centroides = 100    #8
logging.info('Sub Text 1, tam_grupo=%s, n_centroides=%s',tam_grupo, n_centroides)
kt.kmeans_tree(tam_grupo,n_centroides)
logging.info(' ')


# SubText 2
logging.info('------------------------------------------------------------------------')
logging.info(' ')
tam_grupo = 100   #16
n_centroides = 90    #8
logging.info('Sub Text 2, tam_grupo=%s, n_centroides=%s',tam_grupo, n_centroides)
kt.kmeans_tree(tam_grupo,n_centroides)
logging.info(' ')


# SubText 3
logging.info('------------------------------------------------------------------------')
logging.info(' ')
tam_grupo = 100   #16
n_centroides = 80    #8
logging.info('Sub Text 3, tam_grupo=%s, n_centroides=%s',tam_grupo, n_centroides)
kt.kmeans_tree(tam_grupo,n_centroides)
logging.info(' ')


# SubText 4
logging.info('------------------------------------------------------------------------')
logging.info(' ')
tam_grupo = 100   #16
n_centroides = 70    #8
logging.info('Sub Text 4, tam_grupo=%s, n_centroides=%s',tam_grupo, n_centroides)
kt.kmeans_tree(tam_grupo,n_centroides)
logging.info(' ')


# SubText 5
logging.info('------------------------------------------------------------------------')
logging.info(' ')
tam_grupo = 100   #16
n_centroides = 60    #8
logging.info('Sub Text 5, tam_grupo=%s, n_centroides=%s',tam_grupo, n_centroides)
kt.kmeans_tree(tam_grupo,n_centroides)
logging.info(' ')


# SubText 6
logging.info('------------------------------------------------------------------------')
logging.info(' ')
tam_grupo = 100   #16
n_centroides = 50    #8
logging.info('Sub Text 6, tam_grupo=%s, n_centroides=%s',tam_grupo, n_centroides)
kt.kmeans_tree(tam_grupo,n_centroides)
logging.info(' ')


# SubText 7
logging.info('------------------------------------------------------------------------')
logging.info(' ')
tam_grupo = 100   #16
n_centroides = 40    #8
logging.info('Sub Text 7, tam_grupo=%s, n_centroides=%s',tam_grupo, n_centroides)
kt.kmeans_tree(tam_grupo,n_centroides)
logging.info(' ')


# SubText 8
logging.info('------------------------------------------------------------------------')
logging.info(' ')
tam_grupo = 100   #16
n_centroides = 30    #8
logging.info('Sub Text 8, tam_grupo=%s, n_centroides=%s',tam_grupo, n_centroides)
kt.kmeans_tree(tam_grupo,n_centroides)
logging.info(' ')


# SubText 9
logging.info('------------------------------------------------------------------------')
logging.info(' ')
tam_grupo = 100   #16
n_centroides = 20    #8
logging.info('Sub Text 9, tam_grupo=%s, n_centroides=%s',tam_grupo, n_centroides)
kt.kmeans_tree(tam_grupo,n_centroides)
logging.info(' ')