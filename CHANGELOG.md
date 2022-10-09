# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2022-10-09
### Added
- Added models for IATA ONE Record Data Model Ontology v2.0.0 (2022-05-16)
- Added models for IATA ONE Record API Ontology Version v1.1 (2021-04-20)
- Added client for IATA ONE Record API Version v1.1 (2022-05-12)
  - create `LogisticsObject`
  - update `LogisticsObject`
  - get `LogisticsObject`
  - get `LogisticsObjects`
  - create `Event` for `LogisticsObject`
  - get `Events` of `LogisticsObject`
  - send `Notification`
- Added tests for `models`, `ONERecordClient`, and `utils`