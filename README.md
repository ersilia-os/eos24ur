# WHALES scaled

Scaled version of the WHALES descriptors (see eos3ae6). WHALES are holistic molecular descriptors useful for scaffold hopping, based on 3D structure to facilitate natural product featurization. The scaling uses sklearn's Robust Scaler trained on a random set of 100K molecules from ChEMBL.

## Identifiers

* EOS model ID: `eos24ur`
* Slug: `whales-scaled`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Representation`
* Output: `Descriptor`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: Scaled vector representation of a molecule

## References

* [Publication](https://www.nature.com/articles/s42004-018-0043-x)
* [Source Code](https://github.com/grisoniFr/scaffold_hopping_whales)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos24ur)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos24ur.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos24ur) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://www.nature.com/articles/s42004-018-0043-x) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!