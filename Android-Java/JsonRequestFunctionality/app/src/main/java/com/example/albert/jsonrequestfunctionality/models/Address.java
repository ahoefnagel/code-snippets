package com.example.albert.jsonrequestfunctionality.models;

import com.google.gson.annotations.SerializedName;

public class Address {

    @SerializedName("street")
    String street;
    @SerializedName("suite")
    String suite;
    @SerializedName("city")
    String city;
    @SerializedName("zipcode")
    String zipcode;
    @SerializedName("geo")
    Geo geo;

    // All getters
    public String getStreet() {
        return street;
    }

    public String getSuite() {
        return suite;
    }

    public String getCity() {
        return city;
    }

    public String getZipcode() {
        return zipcode;
    }

    public Geo getGeo() {
        return geo;
    }
}
