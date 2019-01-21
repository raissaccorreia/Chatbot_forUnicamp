package br.com.dacbot.dacbotapi.controller;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

/**
 * Controller responsible for returning if application is up
 * 
 * @author gustavovillela
 *
 */
@RestController
@RequestMapping("/health")
public class HealthController {
	
	/**
	 * Method responsible for always return an OK status code
	 */
	@RequestMapping(method=RequestMethod.GET)
	@ResponseStatus(HttpStatus.OK)
	public void health() {
		// no implementation needed
	}
}