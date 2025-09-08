#!/usr/bin/env python3
"""
Project Viktor - Physics AI Explorer Backend
Demo version showcasing core capabilities
"""

import json
import random
import time
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

class PhysicsExplorer:
    def __init__(self):
        self.formulas = self.load_sample_formulas()
        self.current_session = {}
        
    def load_sample_formulas(self):
        """Load our demo formula dataset"""
        # This would normally load from sample_formulas.json
        return [
            {
                "id": "newton_second",
                "name": "Newton's Second Law",
                "equation": "F = ma",
                "domain": "Classical Mechanics",
                "description": "Force equals mass times acceleration",
                "variables": ["F", "m", "a"],
                "applications": ["Motion analysis", "Engineering design"]
            },
            {
                "id": "energy_mass", 
                "name": "Mass-Energy Equivalence",
                "equation": "E = mc²",
                "domain": "Relativity",
                "description": "Energy and mass are interchangeable",
                "variables": ["E", "m", "c"],
                "applications": ["Nuclear physics", "Particle physics"]
            },
            {
                "id": "schrodinger",
                "name": "Schrödinger Equation", 
                "equation": "iℏ ∂ψ/∂t = Ĥψ",
                "domain": "Quantum Mechanics",
                "description": "Fundamental equation of quantum mechanics",
                "variables": ["ψ", "t", "Ĥ", "ℏ"],
                "applications": ["Quantum systems", "Wave functions"]
            }
        ]
    
    def search_formulas(self, query, limit=10):
        """Search formulas using semantic matching"""
        # In the full version, this would use vector embeddings
        results = []
        query_lower = query.lower()
        
        for formula in self.formulas:
            score = 0
            
            # Simple keyword matching for demo
            if query_lower in formula['name'].lower():
                score += 3
            if query_lower in formula['domain'].lower():
                score += 2
            if query_lower in formula['description'].lower():
                score += 1
                
            if score > 0:
                formula_copy = formula.copy()
                formula_copy['relevance_score'] = score
                results.append(formula_copy)
        
        # Sort by relevance
        results.sort(key=lambda x: x['relevance_score'], reverse=True)
        return results[:limit]
    
    def get_formula_relationships(self, formula_id):
        """Find related formulas"""
        # This would use the relationship graph in the full version
        relationships = {
            "newton_second": ["energy_kinetic", "momentum_conservation"],
            "energy_mass": ["energy_kinetic", "momentum_relativistic"], 
            "schrodinger": ["wave_equation", "uncertainty_principle"]
        }
        
        return relationships.get(formula_id, [])
    
    def explain_formula(self, formula_id):
        """Generate AI explanation for a formula"""
        # This would call the local LLM in the full version
        explanations = {
            "newton_second": {
                "explanation": "Newton's Second Law is fundamental to classical mechanics. It tells us that the force acting on an object is directly proportional to its acceleration and mass.",
                "intuition": "Think of pushing a shopping cart - the harder you push (more force), the faster it accelerates. A heavier cart needs more force for the same acceleration.",
                "applications": "Used in engineering design, vehicle dynamics, robotics, and anywhere we need to predict motion."
            },
            "energy_mass": {
                "explanation": "Einstein's famous equation shows that mass and energy are two forms of the same thing. A small amount of mass can be converted to enormous energy.",
                "intuition": "This is why nuclear reactions are so powerful - even tiny amounts of matter release huge energy when converted.",
                "applications": "Nuclear power, particle accelerators, understanding stellar processes, and modern physics."
            }
        }
        
        return explanations.get(formula_id, {
            "explanation": "This formula represents a fundamental relationship in physics.",
            "intuition": "Each variable plays a crucial role in describing the physical phenomenon.",
            "applications": "Used across multiple domains in physics and engineering."
        })

# Initialize our physics explorer
physics_explorer = PhysicsExplorer()

@app.route('/')
def serve_demo():
    """Serve the demo UI"""
    return send_from_directory('.', 'demo_ui.html')

@app.route('/api/search', methods=['POST'])
def search_formulas():
    """Search for physics formulas"""
    try:
        data = request.get_json()
        query = data.get('query', '')
        limit = data.get('limit', 10)
        
        if not query:
            return jsonify({'error': 'Query is required'}), 400
        
        # Simulate processing time
        time.sleep(0.5)
        
        results = physics_explorer.search_formulas(query, limit)
        
        return jsonify({
            'query': query,
            'results': results,
            'total_found': len(results),
            'processing_time': 0.5
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/formula/<formula_id>', methods=['GET'])
def get_formula_details(formula_id):
    """Get detailed information about a specific formula"""
    try:
        # Find the formula
        formula = next((f for f in physics_explorer.formulas if f['id'] == formula_id), None)
        
        if not formula:
            return jsonify({'error': 'Formula not found'}), 404
        
        # Get relationships and explanation
        relationships = physics_explorer.get_formula_relationships(formula_id)
        explanation = physics_explorer.explain_formula(formula_id)
        
        return jsonify({
            'formula': formula,
            'relationships': relationships,
            'ai_explanation': explanation
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/relationships/<formula_id>', methods=['GET'])
def get_formula_relationships(formula_id):
    """Get relationship graph for a formula"""
    try:
        relationships = physics_explorer.get_formula_relationships(formula_id)
        
        # Generate mock 3D coordinates for visualization
        coords = []
        for i, rel_id in enumerate(relationships):
            angle = (i / len(relationships)) * 2 * np.pi
            coords.append({
                'id': rel_id,
                'x': 20 * np.cos(angle),
                'y': 20 * np.sin(angle), 
                'z': random.uniform(-10, 10),
                'connection_strength': random.uniform(0.3, 1.0)
            })
        
        return jsonify({
            'formula_id': formula_id,
            'relationships': coords,
            'total_connections': len(relationships)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/explain', methods=['POST'])
def explain_formula():
    """Get AI explanation for a formula"""
    try:
        data = request.get_json()
        formula_id = data.get('formula_id')
        context = data.get('context', 'general')
        
        if not formula_id:
            return jsonify({'error': 'Formula ID is required'}), 400
        
        # Simulate AI processing time
        time.sleep(1.0)
        
        explanation = physics_explorer.explain_formula(formula_id)
        
        return jsonify({
            'formula_id': formula_id,
            'explanation': explanation,
            'context': context,
            'generated_at': time.time()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats', methods=['GET'])
def get_system_stats():
    """Get system statistics"""
    return jsonify({
        'total_formulas': len(physics_explorer.formulas),
        'domains_covered': len(set(f['domain'] for f in physics_explorer.formulas)),
        'system_status': 'operational',
        'version': '1.0.0-demo'
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': time.time(),
        'version': '1.0.0'
    })

if __name__ == '__main__':
    print("🚀 Starting Project Viktor Demo Server...")
    print("📊 Loaded {} sample formulas".format(len(physics_explorer.formulas)))
    print("🌐 Server running at http://localhost:3001")
    print("🎯 Demo UI available at http://localhost:3001")
    
    app.run(host='0.0.0.0', port=3001, debug=True)