# Detect and Read Handwritten Words

Welcome to the handwritten text recognition (HTR) pipeline, where you can detect and read words in scanned pages with ease.

## Overview

This pipeline utilizes advanced algorithms to perform two main operations:

1. **Word Detection:** The system effectively detects individual words in scanned pages, enabling precise analysis and extraction of text.

2. **Word Reading:** Once the words are detected, the pipeline employs sophisticated techniques to accurately read and interpret the handwritten text, enabling seamless access to the content.

![example](./doc/example.png)

## Installation

To get started, follow these simple installation steps:

1. Navigate to the root directory of the repository.
2. Execute the command `pip install .` to install the necessary dependencies.

## Usage

### Run the Demo

To get a glimpse of the pipeline's capabilities, run the provided demo:

1. Install `matplotlib` for plotting by executing `pip install matplotlib`.
2. Navigate to the `scripts/` directory.
3. Run the command `python demo.py`.
4. Sit back and marvel at the output, which should resemble the plot shown above.

### Use the Python Package

You can also integrate the HTR pipeline into your own projects by following these steps:

1. Import the `read_page` function from the `htr_pipeline` module.
2. Read your image using OpenCV, such as `cv2.imread('data/r06-137.png', cv2.IMREAD_GRAYSCALE)`.
3. Utilize `read_page` to detect and read the text, providing an optional `DetectorConfig` to customize detection settings.
4. Access the extracted text by iterating over the returned `read_lines` object, printing or processing the words as needed.

```python
import cv2
from htr_pipeline import read_page, DetectorConfig

# Read the image
img = cv2.imread('data/r06-137.png', cv2.IMREAD_GRAYSCALE)

# Detect and read text
read_lines = read_page(img, DetectorConfig(height=1000))

# Output the text
for read_line in read_lines:
    print(' '.join(read_word.text for read_word in read_line))
```

Feel free to explore further customization options by referring to the docstrings of `detect` and `sort_multiline` in `htr_pipeline/word_detector/__init__.py`. Notably, the `DetectorConfig` allows adjusting the text height, while the `LineClusteringConfig` offers control over line clustering parameters.

Discover the power of the HTR pipeline, where handwritten words come to life. Unleash the potential of your handwritten documents with ease and precision!


# Detect and Read Handwritten Words

This is a **handwritten text recognition (HTR) pipeline** that operates on **scanned pages** and applies the following
operations:

* Detect words
* Read words

![example](./doc/example.png)


## Installation

* Go to the root level of the repository
* Execute `pip install .`

## Usage

### Run demo

* Additionally install matplotlib for plotting: `pip install matplotlib`
* Go to `scripts/`
* Run `python demo.py`
* The output should look like the plot shown above

### Use Python package

Import the function `read_page` to detect and read text.

````python
import cv2
from htr_pipeline import read_page, DetectorConfig

# read image
img = cv2.imread('data/r06-137.png', cv2.IMREAD_GRAYSCALE)

# detect and read text
read_lines = read_page(img, DetectorConfig(height=1000))

# output text
for read_line in read_lines:
    print(' '.join(read_word.text for read_word in read_line))
````

If needed, the detection can be configured by instantiating and passing these data-classes:

* `DetectorConfig`
* `LineClusteringConfig`

For more details please have a look at the docstrings of `detect` and `sort_multiline`
in `htr_pipeline/word_detector/__init__.py`. The most important settings are:

* `height` in `DetectorConfig`: the word detector is not scale invariant, the text height should be 25-50px when using
  the default parameters, which is achieved by resizing the image to the specified height
* `min_words_per_line` in `LineClusteringConfig`: lines which have fewer words than specified are discarded, the default
  setting is 2, which means that lines with a single word will not be read by default
