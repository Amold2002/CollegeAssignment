package com.entity;

public class User {

	private String Name;
	private String email;
	private String password;
	private String course;

	public String getName() {
		return Name;
	}

	public void setName(String name) {
		Name = name;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public String getCourse() {
		return course;
	}

	public void setCourse(String course) {
		this.course = course;
	}

	public User(String name, String email, String password, String course) {

		Name = name;
		this.email = email;
		this.password = password;
		this.course = course;
	}

	public User() {

	}

}
