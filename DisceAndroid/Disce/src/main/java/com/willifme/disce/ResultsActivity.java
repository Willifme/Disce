package com.willifme.disce;

import android.app.Activity;
import android.os.Build;
import android.os.Bundle;
import android.view.WindowManager;
import android.widget.ImageView;

import org.apache.http.HttpEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.params.BasicHttpParams;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;

/**
 * Created by william on 12/07/13.
 */
public class ResultsActivity extends Activity {

    String URL = null;

    private ImageView mResultsImage;


    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);

        getJSON();

        mResultsImage = (ImageView)findViewById(R.id.image_view);

        getWindow().setSoftInputMode(WindowManager.LayoutParams.SOFT_INPUT_STATE_ALWAYS_HIDDEN); // Hides the keyboard when the activity starts

        // Make sure we're running on Honeycomb or higher to use ActionBar APIs
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {

            // Show the up button in the action bar
            getActionBar().setDisplayHomeAsUpEnabled(true);

        }

        DefaultHttpClient httpClient = new DefaultHttpClient(new BasicHttpParams());

        HttpPost httpPost = new HttpPost(http://86.168.200.197:4000/dog);

        // Depends on your web service
        httpPost.setHeader("Content-type", "applcation/json");

        InputStream inputStream = null;

        String result = null;

        try {

            HttpResponse response = httpClient.execute(httpPost);

            HttpEntity entity = response.getEntity();

            inputStream = entity.getContent();

            // JSON is UTF-8 by defaults
            BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream, "UTF-8"), 8);

            StringBuilder sb = new StringBuilder();

            String line = null;

            while((line = reader.readLine()) != null)
            {

                sb.append(line + "\n");

            }

            result = sb.toString();

        } catch (Exception e) {

            e.printStackTrace();

        }

        finally {

            try { if(inputStream != null) inputStream.close(); } catch(Exception squish){}

        }

        JSONObject jObject = new JSONObject(result);

        String aJsonString = jObject.getString("STRINGNAME");

        boolean aJsonBoolean = jObject.getBoolean("BOOLEANNAME");

        int aJsonInteger = jObject.getInt("INTEGERNAME");

        long aJsonLong = jObject.getBoolean("LONGNAME");

        double aJsonDouble = jObject.getDouble("DOUBLENAME");

        JSONArray jArray = jObject.getJSONArray("ARRAYNAME");

        for (int i=0; i < jArray.length(); i++)
        {
            try {
                JSONObject oneObject = jArray.getJSONObject(i);
                // Pulling items from the array
                String oneObjectsItem = oneObject.getString("STRINGNAMEinTHEarray");
                String oneObjectsItem2 = oneObject.getString("anotherSTRINGNAMEINtheARRAY");
            } catch (JSONException e) {
                // Oops
            }
        }

    }

    public void getJSON() {


    }

}