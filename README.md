# ThresholdEncoder
Simple mapping to keep only certain categorical values from a categorical feature based on their frequency.

**Example:**

Imagine the scenario where you have a categorical feature with high cardinality spread in an imbalanced way.

|  product_code|frequency  |
|--|--|
|c4e18dd6    |0.905883|
|16a36ef3   | 0.005532|
|1e0acfb4  |  0.005515|
|08facbad |   0.003817|
|7e1e7bdf|    0.001857|
|f3ca2e42    |0.001744|
|948ff336    |0.001617|
|ace5b8fd    |0.001604|
|98acf46c    |0.001485|
|7bd4e8cc    |0.001369|
|(..)|(...)|

One approach is to keep the most frequent category along with a couple more based on some pre defined threshold cut point and keeping the others in a seperate *other* category.

This function enables you to create  a mapping to apply on your column and follow up from there.

**Before:**

|  product_code|frequency  |
|--|--|
|c4e18dd6    |0.905883|
|16a36ef3   | 0.005532|
|1e0acfb4  |  0.005515|
|08facbad |   0.003817|
|7e1e7bdf|    0.001857|
|f3ca2e42    |0.001744|
|948ff336    |0.001617|
|ace5b8fd    |0.001604|
|98acf46c    |0.001485|
|7bd4e8cc    |0.001369|
|(..)|(...)|

**After:**

|  product_code|frequency  |
|--|--|
|c4e18dd6   |0.905883|
|16a36ef3    |0.005532|
|1e0acfb4    |0.005515|
|08facbad    |0.003817|
|other      | 0.079254|

# Usage Example

    df = pd.read_csv('data.csv')
    df['product_code'].value_counts(True).head(5)

|  product_code|frequency  |
|--|--|
|c4e18dd6    |0.905883|
|16a36ef3   | 0.005532|
|1e0acfb4  |  0.005515|
|08facbad |   0.003817|
|7e1e7bdf|    0.001857|
|(...)|(...)|

    new_product_map=percentage_encoder(df,'product_code',0.003)
    df['product_code']=df['product_code'].map(lambda x: new_product_map.get(x,'other'))
    df['product_code'].value_counts(True)
|  product_code|frequency  |
|--|--|
|c4e18dd6   | 0.905883
|16a36ef3   | 0.005532
|1e0acfb4  |  0.005515
|08facbad |   0.003817
|other |      0.079254

Created this on a need basis and thought it might suit the purposes of someone else around the web, any tips on doing this some other way are always needed.

Thank you.
