from sklearn.metrics import classification_report
from sklearn.metrics import mean_squared_error
from sklearn.metrics import confusion_matrix
import seaborn as sns

RANDOM_STATE = 2245

LABELS_MAPPING_FORWARD = {
    'national': 0,
    'international': 1,
    'economics': 2,
    'entertainment': 3,
    'sports': 4
}

LABELS_MAPPING_REVERSE = {
    0: 'national', 
    1: 'international', 
    2: 'economics', 
    3: 'entertainment', 
    4: 'sports'
}

NUM_LABELS = len(LABELS_MAPPING_FORWARD)

get_label_name = lambda label_id: LABELS_MAPPING_REVERSE.get(label_id)
get_label_class_id = lambda name: LABELS_MAPPING_REVERSE.get(name)

def get_various_metrics_and_print(Y_true, Y_predicted):
    TN, FP, FN, TP = confusion_matrix(Y_true, Y_predicted).ravel()
    accuracy = (TP + TN)/(TP+TN+FP+FN)
    recall = (TP)/(TP + FN)
    specificity = (TN)/(TN + FP) # TNR
    false_positive_rate = (FP)/(TN + FP) # false_positive_rate = 1 - TNR
    precision = (TP)/(TP + FP)
    false_discovery_rate = (FP)/(TP + FP)
    neg_predicted_val = (TN)/(TN + FN)
    f1_score = 2*((precision * recall) / (precision + recall))

    print("TN = ", TN, " FP = ", FP, " FN = ", FN, " TP = ", TP)
    print("Accuracy = ", accuracy*100, "%")
    print("TPR = Sensitivity = Recall = ", recall*100, "%")
    print("TNR = Specificity = ", specificity*100, "%")
    print("Precision = PPV = Positive Predictive Value = ", precision*100, "%")
    print("FDR = False Discovery Rate = ", false_discovery_rate*100, "%")
    print("FPR = False Positive Rate = ", false_positive_rate*100, "%")
    print("F1 Score = ", f1_score*100, "%")
    print("Neg Predicted Val = ", neg_predicted_val*100, "%")
    print("\n")
    c_report = classification_report(y_true=Y_true, y_pred=Y_predicted)
    print(c_report)
    return precision, recall, f1_score, c_report


def plot_confusion_matrix(Y_true=None, Y_predicted=None):
  ## https://www.youtube.com/watch?v=T27WVIM8Xys
    # mat = confusion_matrix(y_test,y_preds)
    cf_matrix = confusion_matrix(Y_true, Y_predicted)
    # cf_matrix = np.array([[23, 5], [3, 30]])
    print(cf_matrix)
    
    # group_names = ['True Neg','False Pos','False Neg','True Pos']
    group_names = ['TN','FP','FN','TP']
    
    group_counts = ["{0:0.0f}".format(value) for value in cf_matrix.flatten()]
    
    group_percentages = ["{0:.2%}".format(value) for value in cf_matrix.flatten()/np.sum(cf_matrix)]
    
    # labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in zip(group_names,group_counts,group_percentages)]
    labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in zip(group_names,group_counts,group_percentages)]

    labels = np.asarray(labels).reshape(2,2)
    
    # sns.heatmap(cf_matrix/np.sum(cf_matrix), annot=True, 
    #         fmt='.2%', cmap=plt.cm.magma)

    sns.heatmap(cf_matrix, annot=labels, fmt='', cmap=plt.cm.magma)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")