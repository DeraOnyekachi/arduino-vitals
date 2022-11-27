Routes are located in ```backend/views.py```

There is no database for the project because of its small scale so the information is stored in `data.json`

For the `edit-vitals` route, a POST request containing the data of the vitals should be sent in the post request e.g.
```{
    "spo": "10",
    "temp": "10",
    "heartrate": "10"
}```

The `view-vitals` route will GET the information in json form.