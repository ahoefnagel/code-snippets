package com.example.albert.jsonrequestfunctionality.models;

import com.google.gson.annotations.SerializedName;

public class Geo {

    @SerializedName("lat")
    double lat;
    @SerializedName("lng")
    double lng;

    // All getters

    public double getLat() {
        return lat;
    }

    public double getLng() {
        return lng;
    }
}
