# Product Listing Generation – Brief Report

## 1. API Integration

The system uses the OpenAI API to generate product listings from structured input data.

Workflow:
- Input: product metadata (`category`, `color`, `usage`, etc.) + image (`base64`)
- Request: sent to the model via API call
- Output: model generates a product listing in JSON-like format (stored as string in `listing_raw`)
- Storage: results are saved in a pandas DataFrame and exported to a JSON file (`outputs/products_listings.json`)

The integration is executed row-by-row over the dataset.

---

## 2. Challenges

- Handling the model output format stored in `listing_raw` (string containing JSON-like content)
- Converting that output into a valid JSON structure for export

---

## 3. Quality of Generated Listings

Based on sample rows:
- Listings contain structured fields such as `title` and `description`
- Content appears consistent with product attributes (e.g. category, color, usage)
- Output follows a predictable schema across entries

---

## 4. Potential Improvements

- Ensure the model returns strict JSON (without markdown wrappers)
- Validate generated outputs before storing them
- Store parsed JSON directly instead of raw strings
- Optimize processing (e.g. batching API calls)