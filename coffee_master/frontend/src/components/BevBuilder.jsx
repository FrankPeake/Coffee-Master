import React from 'react';
import { Route } from 'react-router-dom';
import './BevBuilder.css';
//I am going to add some sort of footer here to add to all of the pages
function BevBuilder() {
    return (
        <div className>
            <div className='banner'><h1 className='header3'>Beverage Builder</h1><p>Create Your Own Hand-Crafted Beverage</p></div>
            <div className='bevBuilder'>
            <div className='modLeft'>

                <h1>Flavors</h1>
                    <ul className='modification'>
                        <li><label for="quanitity">Mocha</label><input min="0" max="99" type="number" name="quantity"/></li>
                        <li><label for="quanitity">White Mocha</label><input min="0" max="99" type="number" name="quantity"/></li>
                        <li><label for="quanitity">Chai</label><input min="0" max="99" type="number" name="quantity"/></li>
                        <li><label for="quanitity">Vanilla</label><input min="0" max="99" type="number" name="quantity"/></li>
                        <li><label for="quanitity">Hazelnut</label><input min="0" max="99" type="number" name="quantity"/></li>
                        <li><label for="quanitity">Cinnamon Dolce</label><input min="0" max="99" type="number" name="quantity"/></li>
                        <li><label for="quanitity">Toffee Nut</label><input min="0" max="99" type="number" name="quantity"/></li>
                        <li><label for="quanitity">Vanilla (SF)</label><input min="0" max="99" type="number" name="quantity"/></li>
                        <li><label for="quanitity">Cinnamon Dolce (SF)</label><input min="0" max="99" type="number" name="quantity"/></li>
                    </ul>

                    <h1>Milk</h1>
                    <ul className='modification'>
                        <li><label for="quanitity">Whole Milk</label><input type="radio" name="quantity"/></li>
                        <li><label for="quanitity">2% Milk</label><input type="radio" name="quantity"/></li>
                        <li><label for="quanitity">Nonfat Milk</label><input type="radio" name="quantity"/></li>
                        <li><label for="quanitity">Almond Milk</label><input type="radio" name="quantity"/></li>
                        <li><label for="quanitity">Soy Milk</label><input type="radio" name="quantity"/></li>
                        <li><label for="quanitity">Coconut Milk Dolce</label><input type="radio" name="quantity"/></li>
                        <li><label for="quanitity">Oat Milk</label><input type="radio" name="quantity"/></li>
                    </ul>
            </div>
            <div>

            </div>
            <div className='modRight'>
                <h1>Modifications</h1>
                    <ul className='modification'>
                        <li><label for="quanitity">Whipped Cream</label><input type="radio" name="quantity"/></li>
                        <li><label for="quanitity">Caramel Drizzle</label><input type="radio" name="quantity"/></li>
                        <li><label for="quanitity">Mocha Drizzle</label><input type="radio" name="quantity"/></li>
                        <li><label for="quanitity">Upside Down</label><input type="radio" name="quantity"/></li>
                        <li><label for="quanitity">Double Blended</label><input type="radio" name="quantity"/></li>
                        <li><label for="quanitity">Ice</label><input type="radio" name="quantity"/></li>
                        <li><label for="quanitity">Cinnamon</label><input type="radio" name="quantity"/></li>
                        <li><label for="quanitity">Upside Down</label><input type="radio" name="quantity"/></li>
                        <li><label for="quanitity">Double Blended</label><input type="radio" name="quantity"/></li>
                        <li><label for="quanitity">Ice</label><input type="radio" name="quantity"/></li>
                    </ul>

                    <h1>Espresso</h1>
                    <ul className='modification'>
                        <li><label for="quanitity">Signature</label><input min="0" max="99" type="number" name="quantity"/></li>
                        <li><label for="quanitity">Blonde</label><input min="0" max="99" type="number" name="quantity"/></li>
                        <li><label for="quanitity">Affegato</label><input min="0" max="99" type="number" name="quantity"/></li>
                        <li><label for="quanitity">Ristretto</label><input type="radio" name="quantity"/></li>
                        <li><label for="quanitity">Long</label><input type="radio" name="quantity"/></li>
                    </ul>
            </div>

            </div>
            <h1 className='button'>Submit</h1>
        </div>
    );
  }
  
  export default BevBuilder;