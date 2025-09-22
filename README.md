# Danny Wilson Curriculum vitae

> "Do what you can, with what you have, where you are.”
> – Theodore Roosevelt

## Getting started
* This is a CV built using the [YAML Resume spec](https://yamlresume.dev/) and the [YAML Resume CLI](https://yamlresume.dev/docs/cli)
* The source file can be found in [cv.yaml](./cv.yaml) and the [build cv](./pdf/cv-latest.pdf)

## PDF generation
* YAML resume has a prebuilt docker image for building the image
* run `make open-latest` to build the PDF CV and open it

## API
* The CV can be served as JSON via a Fast API application found in [api](./api/)
* run `make install && make api-serve` to install dependencies and start the API server
