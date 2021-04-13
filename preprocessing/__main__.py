from database_methods.database_methods import database_builder
from LogPreprocessor import LogPreprocessor
from WordEmbeddings import WordEmbeddings
import os
import joblib
import time

if __name__ == '__main__':

    # collect logs from database into pandas dataframe
    df = database_builder('/database')


    # create LogPreprocessor object and clean logs and generate templates
    log_preprocessor = LogPreprocessor(df)

    if os.environ["GENERATE_NEW_DRAIN"] == "yes":
        clusters, _ = log_preprocessor.generate_clusters()
    else:
        clusters = joblib.load('/results/clean_clusters.joblib')

    word_embeddings = WordEmbeddings(clusters)
    
    embeddings = word_embeddings.generate_word_embeddings()

    w2v = word_embeddings.word_2_vec


    # "change_type": change_type,
    # "cluster_id": cluster.cluster_id,
    # "cluster_size": cluster.size,
    # "cluster_example": log_message,
    # "template_mined": cluster.get_template(),
    # "cluster_count": len(self.drain.clusters)
    
    # for result in log_preprocessor.results.values():
    #     template = result["template_mined"]
    #     if len(template) < 500:
    #         if re.search(r'(<\*>\s{0,}){1,}', template):
    #             print(f'Cluster Id: {result["cluster_id"]} \n' \
    #                 f'Cluster Example: {result["cluster_example"]} \n' \
    #                 f'Cluster Template: {template} \n\n')

    # for cluster in clusters:
    #     idx = cluster.cluster_id
    #     print(f'template: {cluster.get_template()}\n log: {log_preprocessor} \n\n')