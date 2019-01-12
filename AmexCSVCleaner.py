import AmexTransactionCleaner as transactionCleaner

transactions = transactionCleaner.GetTransactions()

print( transactions )

transactionCleaner.SaveTransactions( transactions )
