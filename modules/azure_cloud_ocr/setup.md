# Azure OCR Setup Guide

## Prerequisites

Before you begin, make sure you have the following:

- An active [Microsoft Azure account](https://azure.microsoft.com).
- Azure for Students (https://azure.microsoft.com/en-us/free/students)

1. **Create an Azure Cognitive Services resource**:
    - Go to the [Azure portal](https://portal.azure.com).
    - Create a new "Cognitive Services" resource.
    - In the search bar, search "Computer Vision" and then create.
    - Pick your subscription.
    - Create a resource group. 
    - Give the project a name.
    - For the pricing tier, choose Standard S1
    - Check the box and then click Review and Create.

2. **Get the API Credentials**:
    - Go to your newly created Cognitive Services resource in the Azure portal.
    - Navigate to the **Keys and Endpoint** section.
    - Copy the **Subscription Key** and **Endpoint URL**. 
    - Add these two lines into your env file.
        AZURE_SUBSCRIPTION_KEY=YOUR_SUBSCRIPTION_KEY
        AZURE_OCR_URL=YOUR_ENDPOINT/vision/v3.2/ocr
