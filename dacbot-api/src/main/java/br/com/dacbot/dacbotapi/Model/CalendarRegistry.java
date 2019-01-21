package br.com.dacbot.dacbotapi.model;

import java.sql.Date;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

/**
 * Class responsible for storing Calendar Registry data
 * @author gustavovillela
 */
@Entity
@Table(name="CALENDAR")
public class CalendarRegistry {
	
	/*
	 * Sequential ID property
	 */
	@Id
	@Column(name="ID")
    @GeneratedValue(strategy=GenerationType.IDENTITY)
	private long id;

	/**
	 * Entity name property
	 */
	@Column(name="ENTITY_STR")
	private String entity;
	
	/**
	 * Year integer property
	 */
	@Column(name="YEAR_INTEGER")
	private int year;

	/**
	 * Semester integer property
	 */
	@Column(name="SEMESTER_INTEGER")
	private int semester;
	
	/**
	 * Initial date property
	 */
	@Column(name="INITIAL_DATE")
	private Date initDate;
	
	/**
	 * End date property
	 */
	@Column(name="END_DATE")
	private Date endDate;
	
	/**
	 * URI string property
	 */
	@Column(name="URI_STR")
	private String uri;
	
	/**
	 * Description string property
	 */
	@Column(name="DESCRIPTION_STR")
	private String description;
	
	public long getId() {
		return id;
	}

	public void setId(long id) {
		this.id = id;
	}
	
	public String getEntity() {
		return entity;
	}

	public void setEntity(String entity) {
		this.entity = entity;
	}

	public int getYear() {
		return year;
	}

	public void setYear(int year) {
		this.year = year;
	}

	public int getSemester() {
		return semester;
	}

	public void setSemester(int semester) {
		this.semester = semester;
	}

	public Date getInitDate() {
		return initDate;
	}

	public void setInitDate(Date initDate) {
		this.initDate = initDate;
	}

	public Date getEndDate() {
		return endDate;
	}

	public void setEndDate(Date endDate) {
		this.endDate = endDate;
	}

	public String getUri() {
		return uri;
	}

	public void setUri(String uri) {
		this.uri = uri;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}
	
}