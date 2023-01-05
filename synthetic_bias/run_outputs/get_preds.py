import json
# from scipy.special import softmax

with open('/Users/xujinghua/irm-for-nli/synthetic_bias/run_outputs/run_output.json') as f:
    d = json.load(f)
    probs = d['results']['predicted probabilities']
    preds = []

    print(len(probs))



    # for prob in probs:
    #     if prob[0] > prob[1]:
    #         preds.append(0)
    #     else:
    #         preds.append(1)
    
    # print(preds)

    