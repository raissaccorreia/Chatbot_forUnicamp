package br.com.dacbot.dacbotapi.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import br.com.dacbot.dacbotapi.model.CalendarRegistry;
import br.com.dacbot.dacbotapi.repository.CalendarRepository;


/**
 * Class responsible for providing Calendar service methods
 * @author gustavovillela
 */
@Service
public class CalendarService {
	
	/**
	 * Calendar repository injection
	 */
	@Autowired
	private CalendarRepository calendarRepository;
	
	/**
	 * Method responsible for getting calendar registry by Id
	 * @param id registry identification
	 */
	public CalendarRegistry getCalendarRegistryById(long id) {		
		// access repository to get and return a calendar registry with the desired ID
		return this.calendarRepository.getOne(id);
	}
	
	/**
	 * Method responsible for getting calendar registry list by entity name
	 * @param entity string containing registry entity name
	 */
	public List<CalendarRegistry> getCalendarRegistryByEntity(String entity) {
		// access repository to get and return a calendar registry with the desired entity name
		return this.calendarRepository.findByEntity(entity);
	}

}
