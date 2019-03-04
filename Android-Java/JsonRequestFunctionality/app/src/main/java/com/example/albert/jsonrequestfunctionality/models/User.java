package com.example.albert.jsonrequestfunctionality.models;

import com.google.gson.annotations.SerializedName;

public class User {

    @SerializedName("id")
    int id;
    @SerializedName("name")
    String name;
    @SerializedName("username")
    String username;
    @SerializedName("email")
    String email;
    @SerializedName("address")
    Address address;
    @SerializedName("phone")
    String phone;
    @SerializedName("company")
    Company company;

    // All getters

    public Company getCompany(){
        return company;
    }

    public String getName() {
        return name;
    }

    public String getEmail() {
        return email;
    }

    public String getPhone() {
        return phone;
    }
}
