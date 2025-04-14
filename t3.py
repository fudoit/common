
import tensorflow as tf

# 假设 name 是你想要提取的特征名称
name = 'feature_name'

# 创建一个示例数据集
data = {
    'feature_name': [1, 2, 3, 4, 5],
    'other_feature': [10, 20, 30, 40, 50]
}
labels = [0, 1, 0, 1, 0]

# 将数据转换为 TensorFlow 数据集
dataset = tf.data.Dataset.from_tensor_slices((data, labels))

# 提取指定特征
feature_ds = dataset.map(lambda x, y: x[name])
print(feature_ds)

# 打印提取的特征
for feature in feature_ds:
    print(feature.numpy())