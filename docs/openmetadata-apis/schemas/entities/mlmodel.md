# MLModel

This schema defines the Model entity. Models are algorithms trained on data to find patterns or make predictions.

**$id:**[**https://open-metadata.org/schema/entity/data/mlmodel.json**](https://open-metadata.org/schema/entity/data/mlmodel.json)

Type: `object`

## Properties
- **id** `required`
  - Unique identifier of a MLModel instance.
  - $ref: [../../type/basic.json#/definitions/uuid](../types/basic.md#uuid)
- **name** `required`
  - Name that identifies this MLModel.
  - Type: `string`
  - Length: between 1 and 64
- **fullyQualifiedName**
  - A unique name that identifies a MLModel.
  - Type: `string`
  - Length: between 1 and 64
- **displayName**
  - Display Name that identifies this MLModel.
  - Type: `string`
- **description**
  - Description of the MLModel, what it is, and how to use it.
  - Type: `string`
- **algorithm** `required`
  - Algorithm used to train the MLModel.
  - Type: `string`
- **mlFeatures**
  - Features used to train the ML Model.
  - Type: `array`
    - **Items**
    - $ref: [#/definitions/mlFeature](#mlfeature)
- **mlHyperParameters**
  - Hyper Parameters used to train the ML Model.
  - Type: `array`
    - **Items**
    - $ref: [#/definitions/mlHyperParameter](#mlhyperparameter)
- **dashboard**
  - Performance Dashboard URL to track metric evolution.
  - $ref: [../../type/entityReference.json](../types/entityreference.md)
- **href**
  - Link to the resource corresponding to this entity.
  - $ref: [../../type/basic.json#/definitions/href](../types/basic.md#href)
- **owner**
  - Owner of this MLModel.
  - $ref: [../../type/entityReference.json](../types/entityreference.md)
- **followers**
  - Followers of this MLModel.
  - $ref: [../../type/entityReference.json#/definitions/entityReferenceList](../types/entityreference.md#entityreferencelist)
- **tags**
  - Tags for this MLModel.
  - Type: `array`
    - **Items**
    - $ref: [../../type/tagLabel.json](../types/taglabel.md)
- **usageSummary**
  - Latest usage information for this MLModel.
  - $ref: [../../type/usageDetails.json](../types/usagedetails.md)
- **version**
  - Metadata version of the entity.
  - $ref: [../../type/entityHistory.json#/definitions/entityVersion](../types/entityhistory.md#entityversion)
- **updatedAt**
  - Last update time corresponding to the new version of the entity.
  - $ref: [../../type/basic.json#/definitions/dateTime](../types/basic.md#datetime)
- **updatedBy**
  - User who made the update.
  - Type: `string`
- **changeDescription**
  - Change that lead to this version of the entity.
  - $ref: [../../type/entityHistory.json#/definitions/changeDescription](../types/entityhistory.md#changedescription)


## Type definitions in this schema

### featureType

- This enum defines the type of data stored in a ML Feature.
- Type: `string`
- The value is restricted to the following: 
  1. _"numerical"_
  2. _"categorical"_

### featureSourceDataType

- This enum defines the type of data of a ML Feature source.
- Type: `string`
- The value is restricted to the following: 
  1. _"integer"_
  2. _"number"_
  3. _"string"_
  4. _"array"_
  5. _"date"_
  6. _"timestamp"_
  7. _"object"_
  8. _"boolean"_


### featureName

- Local name (not fully qualified name) of the ML Feature.
- Type: `string`
- The value must match this pattern: `^[^.]*$`
- Length: between 1 and 64


### featureSourceName

- Local name (not fully qualified name) of a ML Feature source.
- Type: `string`
- The value must match this pattern: `^[^.]*$`
- Length: between 1 and 64


### fullyQualifiedFeatureSourceName

- Fully qualified name of the ML Feature Source that includes `serviceName.[databaseName].tableName/fileName/apiName.columnName[.nestedColumnName]`.
- Type: `string`
- Length: between 1 and 256


### fullyQualifiedFeatureName

- Fully qualified name of the ML Feature that includes `modelName.featureName`.
- Type: `string`
- Length: between 1 and 256


### featureSource

- This schema defines the sources of a ML Feature.
- Type: `object`
- This schema <u>does not</u> accept additional properties.
- **Properties**
  - **name**
    - $ref: [#/definitions/featureSourceName](#featuresourcename)
  - **dataType**
    - Data type of the source (int, date etc.).
    - $ref: [#/definitions/featureSourceDataType](#featuresourcedatatype)
  - **description**
    - Description of the feature source.
    - Type: `string`
  - **fullyQualifiedName**
    - $ref: [#/definitions/fullyQualifiedFeatureSourceName](#fullyqualifiedfeaturesourcename)
  - **tags**
    - Tags associated with the feature source.
    - Type: `array`
      - **Items**
      - $ref: [../../type/tagLabel.json](../types/taglabel.md)


### mlFeature

- This schema defines the type for a ML Feature used in a MLModel.
- Type: `object`
- This schema <u>does not</u> accept additional properties.
- **Properties**
  - **name**
    - $ref: [#/definitions/featureName](#featurename)
  - **dataType**
    - Data type of the column (numerical vs. categorical).
    - $ref: [#/definitions/featureType](#featuretype)
  - **description**
    - Description of the ML Feature.
    - Type: `string`
  - **fullyQualifiedName**
    - $ref: [#/definitions/fullyQualifiedFeatureName](#fullyqualifiedfeaturename)
  - **featureSources**
    - Columns used to create the ML Feature.
    - Type: `array`
      - **Items**
      - $ref: [#/definitions/featureSource](#featuresource)
  - **featureAlgorithm**
    - Description of the algorithm used to compute the feature, e.g., PCA, bucketing...
    - Type: `string`
  - **tags**
    - Tags associated with the feature.
    - Type: `array`
      - **Items**
      - $ref: [../../type/tagLabel.json](../types/taglabel.md)


### mlHyperParameter

- This schema defines the type for a ML HyperParameter used in a MLModel.
- Type: `object`
- This schema <u>does not</u> accept additional properties.
- **Properties**
  - **name**
    - Hyper parameter name.
    - Type: `string`
  - **value**
    - Hyper parameter value.
    - Type: `string`
  - **description**
    - Description of the Hyper Parameter.
    - Type: `string`

_This document was updated on: Monday, November 15, 2021_