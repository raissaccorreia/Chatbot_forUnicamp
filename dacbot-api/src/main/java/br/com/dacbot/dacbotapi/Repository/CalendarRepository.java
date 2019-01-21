package br.com.dacbot.dacbotapi.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
import org.springframework.stereotype.Repository;

import br.com.dacbot.dacbotapi.model.CalendarRegistry;

/**
 * Interface responsible for extending Jpa Repository methods for Calendar operations 
 * @author gustavovillela
 */
@Repository
public interface CalendarRepository extends JpaRepository<CalendarRegistry, Long>, JpaSpecificationExecutor<CalendarRegistry> {
	
	/*
	 * @see org.springframework.data.jpa.repository.JpaRepository#getOne(java.lang.Object)
	 */
	@Override
	CalendarRegistry getOne(Long id);
	
	/**
	 * Method responsible for getting all entities with the received name
	 * @param entity to be find
	 * @return list of entities
	 */
	List<CalendarRegistry> findByEntity(String entity);
}