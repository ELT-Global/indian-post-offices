# All India Pincode Directory

The dataset for this can be downloaded from [here](https://www.data.gov.in/resource/all-india-pincode-directory-till-last-month).

This repository contains the code to clean the CSV data and convert it into a JSON format (optimized for MongoDB) conforming to the following schema:

```ts
interface PostOffice {
    state: string;
    district: string;
    offices: string[];
}
```

## Necessity

This is useful for applications where we need to auto-fill the area, district, and state based on the pincode entered by the user. This can be used in e-commerce websites, address forms, etc.

## 🚀 Getting Started

1. **Clone the repository.**

    ```sh
    git clone https://github.com/ELT-Global/indian-post-offices.git
    ```

2. **Download the dataset.**

    Download the dataset from [here](https://www.data.gov.in/resource/all-india-pincode-directory-till-last-month).
    If not found, you will have to search for it in [data.gov.in](https://www.data.gov.in/search?title=pincode&type=resources&sortby=_score)

3. **Run the script.**

    ```sh
    python converter.py <path-to-csv-file> <path-to-output-file>
    ```

    This will generate a JSON output file in the same directory.
