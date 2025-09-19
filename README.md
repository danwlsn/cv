# Danny Wilson Curriculum vitae

> "Do what you can, with what you have, where you are.”
> – Theodore Roosevelt

## Getting started
* This is a CV built using the [YAML Resume spec](https://yamlresume.dev/)
* The source file can be found in [cv.yaml](./cv.yaml)

## PDF generation
* YAML resume has a prebuilt docker image for building the image
* run `make build` to build a new version of the CV PDF

## API
* The CV can be served as JSON via a Fast API application found in [api](./api/)
* run `make api-serve` to start the API server
