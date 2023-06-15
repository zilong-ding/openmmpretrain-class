import splitfolders

# train:validation:test=8:1:1
splitfolders.ratio(input='./data/fruit30_train', output='./output', seed=1337, ratio=(0.8, 0.1, 0.1))

