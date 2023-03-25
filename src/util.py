'''
    dserve
    https://github.com/loretoparisi/dserve
    @2023 loretoparisi@gmail.com
'''
def tolabels(predictions, decimal_places = 2):
    labels = {}
    # predictions are ordered to max prob
    int2label_dict = predictions[0]
    for (index, value) in enumerate(predictions[1]):
        label = int2label_dict[index].replace('__label__', '')
        labels[label] = round(value, decimal_places)
    return labels