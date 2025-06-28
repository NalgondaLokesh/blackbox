#!/bin/bash

# Health Check
curl -X GET "http://localhost:5010/ping"

# Obfuscate Test
curl -X POST "http://localhost:5010/v1/obfuscate" \
  -H "Content-Type: application/json" \
  -d '{"data":"test123"}'

# Quantum Test  
curl -X POST "http://localhost:5010/v1/quantum" \
  -H "Content-Type: application/json" \
  -d '{"magic":true, "x":42}'

# [Add test commands for all endpoints...]