package com.example.albert.jsonrequestfunctionality.models;

import com.google.gson.annotations.SerializedName;

public class Company {

    @SerializedName("name")
    String name;
    @SerializedName("catchPhrase")
    String catchPhrase;
    @SerializedName("bs")
    String bs;

    // All getters

    public String getName() {
        return name;
    }

    public String getCatchPhrase() {
        return catchPhrase;
    }

    public String getBs() {
        return bs;
    }
}
