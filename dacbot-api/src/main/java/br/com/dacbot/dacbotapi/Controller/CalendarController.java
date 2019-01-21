package br.com.dacbot.dacbotapi.controller;

import java.util.List;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import br.com.dacbot.dacbotapi.model.CalendarRegistry;
import br.com.dacbot.dacbotapi.service.CalendarService;

/**
 * Controller responsible for responding Calendar requests
 * 
 * @author gustavovillela
 *
 */
@RestController
@RequestMapping("/calendar")
public class CalendarController {
	
	/**
	 * Reference to Calendar Service 
	 */
	@Autowired
	private CalendarService calendarService;
	
	/**
	 * Method responsible for getting a calendar registry by its ID
	 * @param id sequential id number 
	 */
	@RequestMapping(path= "/{id}", method=RequestMethod.GET)
	@ResponseStatus(value = HttpStatus.OK)
	private CalendarRegistry getCalendarRegitryById (@PathVariable Long id) {		
		// return the found entity
		return this.calendarService.getCalendarRegistryById(id);
	}
	
	/**
	 * Method responsible for getting a calendar registry list by an entity name
	 * @param entity string with entity name
	 */
	@RequestMapping(method=RequestMethod.GET)
	@ResponseStatus(value = HttpStatus.OK)
	private List<CalendarRegistry> getCalendarRegitry (@Valid @RequestParam(value="entity") String entity) {		
		// return a list of found entities
		return this.calendarService.getCalendarRegistryByEntity(entity);
	}

}
