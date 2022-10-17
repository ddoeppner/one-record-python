# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v0.2.0] - 2022-10-17
### Added
- added client function to update `LogisticsObject`
- added mocked unit tests for `ONERecordClient`
- added enums for cargo ontology, e.g. `WaybillType`, `SensorType`, or `PartyRole`

## [v0.1.0] - 2022-10-09
### Added
- added models for IATA ONE Record Data Model Ontology v2.0.0 (2022-05-16)
- added models for IATA ONE Record API Ontology Version v1.1 (2021-04-20)
- added client for IATA ONE Record API Version v1.1 (2022-05-12)
  - create `LogisticsObject`
  - get `LogisticsObject`
  - get `LogisticsObjects`
  - create `Event` for `LogisticsObject`
  - get `Events` of `LogisticsObject`
  - send `Notification`
- added tests for `models`, `ONERecordClient`, and `utils`