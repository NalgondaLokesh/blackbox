# Black Box API Documentation

## Endpoint Behaviors

### 1. `GET /ping`
- **Behavior**: Basic health check
- **Response**: 
  ```json
  {"status": "active", "time": "HH:MM:SS"}
  ```

### 2. `POST /v1/obfuscate`
- **Input**: {"data": "text"}
- **Behavior**: Applies ROT5 to digits + Base64 encoding
- **Response**:
  ```json
  {"result": "encoded_string", "hint": "Digits are shifted before encoding"}
  ```

### 3. `POST /v1/quantum`
- **Input**: Any JSON
- **Secret Triggers**:
  - Key named "magic"
  - Value equals "42"
- **Response**:
  ```json
  {"observations": [{"phenomenon": "quantum_effect"}, ...]}
  ```

[... Document all 10 endpoints ...]

## Discovery Techniques
1. **Input Variation**: Try different data types
2. **Time-Based**: Some endpoints change behavior hourly
3. **Header Inspection**: Check for hidden response hints