# Calling OpenAI Batch steps

Guide to OpenAI batch api --> https://platform.openai.com/docs/guides/batch

---

## Step 1: Prepare Batch File (prepare_batch.py)

   1. Prepare a .jsonl file containing your batch requests. Each line represents a single API request.
   2. Usage: Run the script to process all files in the specified directory and generate the batch file.

---

## Step 2: Upload Batch File (upload_batch_file.py)

   1. Upload the prepared batch file to OpenAI using the Files API. 
   2. The script uploads batch_input.jsonl and returns the file ID.

---

## Step 3: Create Batch (create_batch.py)

   1. Create a batch job using the uploaded file's ID. Add the file ID obtained from running upload_batch_file.py to create_batch.py.
   2. Returns a batch ID.

---

## Step 4: Check Batch Status (check_batch_status.py)

   1. Use the batch iD from create_batch.py to check the status of the batch job to monitor progress.
      Possible statuses:
         1. validating: Validating the input file.
         2. in_progress: Batch is running.
         3. completed: Batch is finished and results are ready.
         4. failed: Validation failed.
         5. expired: Batch did not complete within the window.
   2. Retrieves the output_file_ID if completed.

---

## Step 5: Retrieve Results (retrieve_results.py)

   1. Download the results using the output_file_id retrieved from the batch status.

---

## Helper scripts

   1. Cancel Batch (cancel_batch.py)
      1. Cancel an ongoing batch if required. Changes batch status to cancelling and eventually cancelled.

   2. List Batches (list_batches.py)
      1. View all batches created, including their status and metadata.

## Consolidated script that combines all the functionalities (Except helpers)

   1. batch_processing.py
      - need to add in folder path of your folder of deeds